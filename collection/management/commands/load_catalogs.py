import csv
import os
from django.conf import settings
from django.core.management.base import BaseCommand
from collection.models import ColorsNcs, ColorsPantone, ColorsRalClassic, ColorsRalDesign, ColorsRalEffect

class Command(BaseCommand):
    help = 'Load color collections from CSV files'

    def handle(self, *args, **kwargs):
        BASE_DIR = settings.BASE_DIR
        base_dir = os.path.join(BASE_DIR, 'csv_file')
        collection_files = {
            'colors_ncs.csv': ColorsNcs,
            'colors_pantone.csv': ColorsPantone,
            'colors_ral_classic.csv': ColorsRalClassic,
            'colors_ral_design.csv': ColorsRalDesign,
            'colors_ral_effect.csv': ColorsRalEffect
        }
        
        for file_name, model in collection_files.items():
            file_path = os.path.join(base_dir, file_name)
            if os.path.exists(file_path):
                with open(file_path, newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    
                    if model in [ColorsNcs, ColorsPantone]:
                        required_fields = {'bgcolor', 'name', 'value1', 'value2', 'value3', 'value4', 'hex', 'r', 'g', 'b'}
                    elif model == ColorsRalClassic:
                        required_fields = {'bgcolor', 'ral_code', 'name', 'cmyk_coated', 'cmyk_uncoated', 'html_hex', 'rgb'}
                    elif model in [ColorsRalDesign, ColorsRalEffect]:
                        required_fields = {'bgcolor', 'id', 'name', 'cymk', 'rgb_percentage', 'hex', 'rgb_values'}
                    
                    missing_fields = required_fields - set(reader.fieldnames)
                    if missing_fields:
                        self.stdout.write(self.style.ERROR(f'File {file_name} does not contain the required fields: {missing_fields}'))
                        continue

                    for row in reader:
                        try:
                            if model in [ColorsNcs, ColorsPantone]:
                                model.objects.create(
                                    bgcolor=row.get('bgcolor'),
                                    name=row['name'],
                                    value1=row.get('value1'),
                                    value2=row.get('value2'),
                                    value3=row.get('value3'),
                                    value4=row.get('value4'),
                                    hex_code=row.get('hex'),  # Updated to 'hex'
                                    r=int(row.get('r', 0)) if row.get('r') else None,
                                    g=int(row.get('g', 0)) if row.get('g') else None,
                                    b=int(row.get('b', 0)) if row.get('b') else None
                                )
                            elif model == ColorsRalClassic:
                                model.objects.create(
                                    bgcolor=row.get('bgcolor'),
                                    ral_code=row['ral_code'],
                                    name=row['name'],
                                    cmyk_coated=row.get('cmyk_coated'),
                                    cmyk_uncoated=row.get('cmyk_uncoated'),
                                    html_hex=row.get('html_hex'),
                                    rgb=row.get('rgb')
                                )
                            elif model in [ColorsRalDesign, ColorsRalEffect]:
                                model.objects.create(
                                    bgcolor=row.get('bgcolor'),
                                    ral_id=row['id'],
                                    name=row['name'],
                                    cymk=row.get('cymk'),
                                    rgb_percentage=row.get('rgb_percentage'),
                                    hex_code=row.get('hex'),  # Updated to 'hex'
                                    rgb_values=row.get('rgb_values')
                                )
                        except KeyError as e:
                            self.stdout.write(self.style.ERROR(f'Missing expected field {e} in file {file_name} for row {row}'))
                        except ValueError as e:
                            self.stdout.write(self.style.ERROR(f'Value error: {e} in file {file_name} for row {row}'))
            else:
                self.stdout.write(self.style.ERROR(f'File {file_name} not found in {base_dir}'))

            self.stdout.write(self.style.SUCCESS(f'Successfully loaded {file_name}'))