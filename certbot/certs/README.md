(From https://www.ibm.com/docs/en/api-connect/2018.x?topic=overview-generating-self-signed-certificate-using-openssl)

# Generate self-signed certs key.pem and certificate.pem

        openssl req -newkey rsa:2048 -nodes -keyout key.pem -x509 -days 365 -out certificate.pem

# View the certificate.pem

        openssl x509 -text -noout -in certificate.pem

# Combine the two into p12 cert, if required

        openssl pkcs12 -inkey key.pem -in certificate.pem -export -out certificate.p12
