def download_file(message, folder_name, progress_callback=None):
    try:
        file_size = (
            message.video.size
            if message.video
            else message.document.size if message.document else 0
        )

        if progress_callback:
            progress_callback(0, file_size)

        # Simulate downloading the file
        # This is where the actual download logic would go
        for current in range(0, file_size, 1024):  # Simulating chunks of 1KB
            if progress_callback:
                progress_callback(current, file_size)

        # Final callback to indicate completion
        if progress_callback:
            progress_callback(file_size, file_size)

    except Exception as e:
        print(f"Error downloading media: {e}")