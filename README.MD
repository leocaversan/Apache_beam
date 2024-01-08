# Apache Beam

## to use apache spark as "runner". Necessary run the apache spark in a container.

````
docker run --net=host apache/beam_spark_job_server:latest


import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

options = PipelineOptions([
    "--runner=PortableRunner",
    "--job_endpoint=localhost:8099",
    "--environment_type=LOOPBACK"
])
````
other exemple

````
docker run --net=host apache/beam_spark_job_server:latest


import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

options = PipelineOptions(
    runner='DataflowRunner',
    project='my-project-id',
    job_name='unique-job-name',
    temp_location='gs://my-bucket/temp',
)
````


