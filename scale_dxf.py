import ezdxf

def scale_dxf_file(input_file, output_file, scale_factor):
    # Load the input DXF file
    doc = ezdxf.readfile(input_file)

    # Get the model space layout
    modelspace = doc.modelspace()

    # Apply scaling to each entity in the model space
    for entity in modelspace:
        entity.scale(scale_factor)

    # Save the modified DXF file
    doc.saveas(output_file)

# Example usage
input_file = 'input.dxf'
output_file = 'output.dxf'
scale_factor = 1/8  # Set the desired scale factor here

scale_dxf_file(input_file, output_file, scale_factor)
