import hashlib
def get_file_hash(file_path, algorithm='sha256'):
    """Calculates the hash of a file's content."""
    hasher = hashlib.new(algorithm)
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(4096)  # Read in 4KB chunks
            if not chunk:
                break
            hasher.update(chunk)
    return hasher.hexdigest()