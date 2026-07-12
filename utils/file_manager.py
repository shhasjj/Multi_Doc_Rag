import os


UPLOAD_FOLDER = "data"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def save_uploaded_files(uploaded_files):
    saved_paths = []

    for uploaded_file in uploaded_files:
        file_path = os.path.join(
            UPLOAD_FOLDER,
            uploaded_file.name
        )

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        saved_paths.append(file_path)

    return saved_paths