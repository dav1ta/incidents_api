# Build
docker build -t incidents .
# Run
docker run -p 8000:8000 incidents

## simple solution with django rest api and viewsets


#URLS and examples

- incidents
  - http://localhost:8000/api/v1/incidents/
- targets - objects
  - http://localhost:8000/api/v1/targets/
- cve-codes
  - http://localhost:8000/api/v1/cve/
- incident-descriptions
  - http://localhost:8000/api/v1/incident-descriptions/
## filtering done with query parameters
- filtering example
  - http://localhost:8000/api/v1/incidents/?start_date=2022-10-22%2009:21:46&end_date=2022-10-22%2020:22:09&cve=CVE-2021-1543


## Deletion or update example
http://localhost:8000/api/v1/cve/<id>
