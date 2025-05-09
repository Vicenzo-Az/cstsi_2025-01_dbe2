#!/bin/sh
until pg_isready -h postgres -p 5432; do
  echo "Aguardando Postgres..."
  sleep 2
done
echo "Postgres está pronto!"