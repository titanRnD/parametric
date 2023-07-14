import ezdxf

# Example usage
length = 4
width = 4
center_hole_diameter = 2.8  # Large hole diameter for bolts
corner_radius = 0.25
bolt_hole_diameter = 0.32  # Diameter of the smaller corner holes for bolts
export_path = f'export_flange_{length}-x-{width}-o-{center_hole_diameter}.dxf'

def generate_line_drawing(length, width, center_hole_diameter, corner_radius, bolt_hole_diameter, export_path):
    # Create a new DXF document
    doc = ezdxf.new(dxfversion='R2010')

    # Create a new modelspace in the DXF document
    modelspace = doc.modelspace()

    # Calculate the dimensions for the line drawing
    half_length = length / 2
    half_width = width / 2

    # Define the corner points of the rectangle with radiused corners
    top_left = (-half_length + corner_radius, half_width - corner_radius)
    top_right = (half_length - corner_radius, half_width - corner_radius)
    bottom_left = (-half_length + corner_radius, -half_width + corner_radius)
    bottom_right = (half_length - corner_radius, -half_width + corner_radius)

    # Draw the rectangle with radiused corners
    modelspace.add_arc(top_left, corner_radius, 90, 180)
    modelspace.add_arc(top_right, corner_radius, 0, 90)
    modelspace.add_arc(bottom_right, corner_radius, 270, 360)
    modelspace.add_arc(bottom_left, corner_radius, 180, 270)
    modelspace.add_line((top_left[0], top_left[1] + corner_radius), (top_right[0], top_right[1] + corner_radius))
    modelspace.add_line((top_right[0] + corner_radius, top_right[1]), (bottom_right[0] + corner_radius, bottom_right[1]))
    modelspace.add_line((bottom_right[0], bottom_right[1] - corner_radius), (bottom_left[0], bottom_left[1] - corner_radius))
    modelspace.add_line((bottom_left[0] - corner_radius, bottom_left[1]), (top_left[0] - corner_radius, top_left[1]))

    # Draw the center hole
    center_hole_radius = center_hole_diameter / 2
    modelspace.add_circle((0, 0), center_hole_radius)

    # Draw the bolt holes in the corners
    bolt_hole_radius = bolt_hole_diameter / 2
    hole_offset = .2
    hole_points = [
        (top_left[0] + hole_offset, top_left[1] - hole_offset),
        (top_right[0] - hole_offset, top_right[1] - hole_offset),
        (bottom_right[0] - hole_offset, bottom_right[1] + hole_offset),
        (bottom_left[0] + hole_offset, bottom_left[1] + hole_offset)
    ]
    for point in hole_points:
        modelspace.add_circle(point, bolt_hole_radius)

    # Save the DXF file
    doc.saveas(export_path)

    # Inform the user about the successful export
    print(f'{export_path} exported successfully.')


generate_line_drawing(length, width, center_hole_diameter, corner_radius, bolt_hole_diameter, export_path)

