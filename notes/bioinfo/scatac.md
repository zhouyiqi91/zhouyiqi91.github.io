From the log:
  [E::hts_tpool_init] Couldn't start thread pool worker : Operation not permitted
  samtools sort: failed to set up thread pool: Operation not permitted

I can't reproduce the error on our local server or github actions.
Maybe there is not enough memory
https://github.com/samtools/samtools/issues/690
or it has something to do with the docker version. The docker version on our local server is 26.1.0.
https://stackoverflow.com/questions/76703987/rabbitmq-docker-failed-to-create-thread-operation-not-permitted-1

