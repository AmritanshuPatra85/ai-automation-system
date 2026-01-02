import os
import shutil


def organize_by_file_type(folder_path):
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        if os.path.isdir(item_path):
            continue

        _, extension = os.path.splitext(item)
        folder_name = extension[1:] if extension else "no_extension"
        destination_folder = os.path.join(folder_path, folder_name)

        os.makedirs(destination_folder, exist_ok=True)
        shutil.move(item_path, os.path.join(destination_folder, item))

    return {
        'success': True,
        'message': 'Folder organized successfully'
    }


def bulk_rename(folder_path, prefix):
    renamed_files = 0

    for filename in os.listdir(folder_path):
        old_path = os.path.join(folder_path, filename)

        if not os.path.isfile(old_path):
            continue

        if filename.startswith(prefix):
            continue

        new_name = prefix + filename
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)
        renamed_files += 1

    return {
        'success': True,
        'message': f'Renamed {renamed_files} files with prefix "{prefix}"'
    }