import barcode
import barcode.writer


def generate_barcode(data, filename="barcode"):
    """
    Generates a barcode and saves it as an image file.

    :param data: The data to encode in the barcode.
    :param filename: The name of the output image file (without extension).
    """
    try:
        # Select the EAN13 barcode format
        barcode_format = barcode.get_barcode_class("ean13")

        # Create the barcode
        barcode_obj = barcode_format(data, writer=ImageWriter())

        # Save the barcode as an image
        output_file = barcode_obj.save(filename)

        print(f"Barcode saved as {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    # Data must be 12 numeric characters for EAN-13 format
    data = "123456789012"  # Replace with your data
    generate_barcode(data, "my_barcode")
