"""Constants used in Mackup."""
# Current version
VERSION = "0.8.27"

# Support platforms
PLATFORM_DARWIN = "Darwin"
PLATFORM_LINUX = "Linux"

# Directory containing the application configs
APPS_DIR = "applications"

# Mackup application name
MACKUP_APP_NAME = "mackup"

# Default Mackup backup path where it stores its files in Dropbox
MACKUP_BACKUP_PATH = "Mackup"

# Mackup config file
MACKUP_CONFIG_FILE = ".mackup.yaml"
MACKUP_OLD_CONFIG_FILE = ".mackup.cfg"

# Old and new file extensions for the config files
MACKUP_CONFIG_EXTENSION = ".yaml"
MACKUP_OLD_CONFIG_EXTENSION = ".cfg"

# Directory that can contains user defined app configs
CUSTOM_APPS_DIR = ".mackup"

# Supported engines
ENGINE_BOX = "box"
ENGINE_COPY = "copy"
ENGINE_DROPBOX = "dropbox"
ENGINE_FS = "file_system"
ENGINE_GDRIVE = "google_drive"
ENGINE_ICLOUD = "icloud"

MACKUP_USER_CONFIG_SCHEMA = "schemas/user.yaml"
MACKUP_APP_CONFIG_SCHEMA = "schemas/app.yaml"
