from deid.dicom import get_files, replace_identifiers, get_identifiers, clean_pixel_data, DicomCleaner
from deid.utils import get_installdir
from deid.data import get_dataset
from deid.config import DeidRecipe
from deid.logger.message import bot
from pydicom import read_file, dataset
from pprint import pprint
import os
import secrets


if __name__ == "__main__":
    
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, r'data')
    if not os.path.exists(final_directory): os.makedirs(final_directory)
    input_dir=f'data/input/'
    output_dir=f'data/output/'
    input_files=list(get_files(input_dir))

    bot.log("Discovering DICOM files")
    for file in input_files:
        dicom = read_file(file)    
        print(f"###DICOM File: {os.path.basename(file)}:{dicom.get('PatientID')} - {dicom.get('PatientName')} - {dicom.get('PatientSex')} \n {dicom.get('PhotometricInterpretation')}")

    cleaner = DicomCleaner()
    ifile=0
    for file in input_files:
        ifile+=1
        try:
            dicom=read_file(file)
            print(f"### Reading DICOM File {ifile}/{len(input_files)}: {os.path.basename(file)}:{dicom.get('PatientID')} - {dicom.get('PatientName')} - {dicom.get('PatientSex')}")
        except Exception as e:
            bot.warning(f"Error reading file {file}")
        try:
            detected = cleaner.detect(file)
            pprint(detected)
            cleaned = cleaner.clean(fix_interpretation=False)
            cleaner.save_dicom(output_folder=output_dir)
        except Exception as e:
            bot.warning("### START ERROR CLEANING PIXELS###")
            print(e)
            bot.warning("### END ERROR CLEANING PIXELS###")

    output_files=list(get_files(output_dir))
    
    bot.log("Getting current identifiers" )
    #Get real patient identifiers
    ids = get_identifiers(output_files)

    bot.log("Removing identifiers")
    #Remove patient identifiers
    files_ids_removed = replace_identifiers(
        dicom_files=output_files, 
        ids=ids,
        save=True,
        overwrite=True
    )

    bot.log(f"Identifiers removed from {len(files_ids_removed)} files.")
    bot.log(f"Anonymization complete. Files have been written to {output_dir}")
