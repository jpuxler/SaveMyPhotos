from pyicloud import PyiCloudService
import os


# Deine iCloud-Zugangsdaten
icloud_username = 'jpuxler@icloud.com'
password = 'E$i#GC2rrCJi02D7'
# Verzeichnis auf deinem Computer, in das die Bilder gespeichert werden sollen
download_directory = '../testBilder/'


# Verbindung zur iCloud herstellen
api = PyiCloudService(icloud_username, password)

if api.requires_2fa:
    print("Two-factor authentication required.")
    code = input("Enter the code you received of one of your approved devices: ")
    result = api.validate_2fa_code(code)

    if not result:
        print("Failed to verify security code")
        sys.exit(1)

    if not api.is_trusted_session:
        print("Session is not trusted. Requesting trust...")
        result = api.trust_session()
        print("Session trust result %s" % result)

        if not result:
            print("Failed to request trust. You will likely be prompted for the code again in the coming weeks")
if api.requires_2sa:
    import click
    print("Two-step authentication required. Your trusted devices are:")

# Liste der verfügbaren Fotos abrufen
photos = api.photos.albums['Snapchat']

photo = next(iter(photos), None)



# Sicherstellen, dass das Download-Verzeichnis existiert
os.makedirs(download_directory, exist_ok=True)

# Fotos herunterladen
for photo in photos:
    download = photo.download()
    with open(download_directory+photo.filename, 'wb') as opened_file:
        opened_file.write(download.raw.read())
    print(f"Bild {photo.id} heruntergeladen.")
print("Download abgeschlossen.")

