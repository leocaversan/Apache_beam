import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.options.pipeline_options import PipelineOptions

pipeline_options = PipelineOptions(argv=None)
pipeline = beam.Pipeline(options=pipeline_options)

sociosColNames = [
    'cnpj_basico', 
    'identificador_de_socio', 
    'nome_do_socio_ou_razao_social', 
    'cnpj_ou_cpf_do_socio', 
    'qualificacao_do_socio', 
    'data_de_entrada_sociedade', 
    'pais', 
    'representante_legal', 
    'nome_do_representante', 
    'qualificacao_do_representante_legal', 
    'faixa_etaria'
    ]

temp_dict = {}
def create_dict_of_arrays(dicts:dict):
    
    return (dicts['cnpj_basico']+'--'+dicts['data_de_entrada_sociedade'],dicts)
    

read_and_transofrm = (
    pipeline
    | "Read text file" >> ReadFromText('data/test.txt', skip_header_lines=1)
    | "Split the line into list of strings" >> beam.Map(lambda x: x.split(';'))
    | "Transform the lists into dictionarys" >> beam.Map(lambda x: dict(zip(sociosColNames, x)))
    | "Transform the dictionarys into a list of dictionaries" >> beam.ParDo(create_dict_of_arrays)
)

show = (
    read_and_transofrm
    | "show the rotws in dict form" >> beam.Map(print)
)

pipeline.run()