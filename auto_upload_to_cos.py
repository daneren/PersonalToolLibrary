import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from tencentcloud.cos import CosClient
from tencentcloud.common import Credential
import pyperclip


class PDFUploader(FileSystemEventHandler):
    """A handler for watching a directory and uploading new PDF files to Tencent COS."""

    def __init__(self, secret_id, secret_key, region, bucket):
        """Initialize the uploader with Tencent COS credentials."""
        self.cos_client = CosClient(secret_id, secret_key, region)
        self.bucket = bucket

    def on_created(self, event):
        """Handle a file creation event."""
        if not event.is_directory and event.src_path.endswith('.pdf'):
            self.upload_to_cos(event.src_path)

    def upload_to_cos(self, file_path):
        """Upload a file to Tencent COS and copy its URL to the clipboard."""
        # Upload the file to Tencent COS
        self.cos_client.upload_file(
            Bucket=self.bucket,
            LocalFilePath=file_path,
            Key=os.path.basename(file_path),
            PartSize=1,
            MAXThread=10,
            EnableMD5=False
        )

        # Generate the file's URL
        url = f"https://{self.bucket}.cos.{region}.myqcloud.com/{os.path.basename(file_path)}"

        # Copy the URL to the clipboard
        pyperclip.copy(url)


def watch_directory(directory, event_handler):
    """Start watching a directory with the given event handler."""
    # Start the file watcher
    observer = Observer()
    observer.schedule(event_handler, path=directory, recursive=False)
    observer.start()

    # Keep the script running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


def start_watching(secret_id, secret_key, region, bucket, directory):
    """Create a PDFUploader and start watching a directory."""
    # Create the event handler
    event_handler = PDFUploader(secret_id, secret_key, region, bucket)

    # Start watching the directory
    watch_directory(directory, event_handler)


if __name__ == "__main__":
    # Replace these with your own Tencent COS credentials and the directory to watch
    secret_id = 'YOUR_SECRET_ID'
    secret_key = 'YOUR_SECRET_KEY'
    region = 'REGION'
    bucket = 'your-bucket-name'
    directory = 'your-directory-to-watch'

    start_watching(secret_id, secret_key, region, bucket, directory)
