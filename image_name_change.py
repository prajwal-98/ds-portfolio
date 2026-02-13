import os
from pathlib import Path

def rename_images(directory_path, base_name="image"):
    try:
        # Convert to Path object for cross-platform compatibility
        folder = Path(directory_path)
        
        if not folder.is_dir():
            print(f"Error: The directory {directory_path} does not exist.")
            return

        # Supported image extensions
        extensions = {'.jpg', '.jpeg', '.png', '.webp', 'heic'}
        
        # Filter and sort files to maintain order
        files = sorted([f for f in folder.iterdir() if f.suffix.lower() in extensions])
        
        if not files:
            print("No images found in the specified directory.")
            return

        print(f"Renaming {len(files)} images...")

        for index, file_path in enumerate(files, start=1):
            # Construct new filename: image-1.jpg, image-2.jpg, etc.
            new_name = f"{base_name}-{index}{file_path.suffix}"
            new_path = folder / new_name
            
            # Prevent overwriting if file already exists
            if new_path.exists():
                print(f"Skipping {new_name}: File already exists.")
                continue
                
            file_path.rename(new_path)
            
        print("Batch renaming completed successfully.")

    except PermissionError:
        print("Error: Permission denied. Close any applications using these files.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Replace with your actual folder path
    target_folder = r"D:\media\photo to portfolio"
    rename_images(target_folder)