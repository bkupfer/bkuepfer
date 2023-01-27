from dog_names import DOG_NAMES
from bing_image_downloader import downloader

for dog in DOG_NAMES:
    downloader.download(
        dog,
        limit=6,
        output_dir='static/dogo_pictures',
        adult_filter_off=True,
        force_replace=False,
        timeout=120,
        verbose=True
    )
