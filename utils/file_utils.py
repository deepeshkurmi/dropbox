import os

class FileUtils:
    @staticmethod
    def save_file(file_data, file_name):
        """
        Save the uploaded file to the specified directory.

        Args:
            file_data (UploadedFile): The file data to be saved.
            file_name (str): The name of the file.

        Returns:
            str: The path where the file is saved.
        """
        # Define the directory where files will be saved
        save_directory = 'assets/uploaded_files'

        # Create the directory if it doesn't exist
        os.makedirs(save_directory, exist_ok=True)

        # Construct the full file path
        file_path = os.path.join(save_directory, file_name)

        # Open the file and write the chunks of data
        with open(file_path, 'wb') as destination:
            for chunk in file_data.chunks():
                destination.write(chunk)

        return file_path
