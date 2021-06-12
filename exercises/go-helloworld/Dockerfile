FROM golang:alpine
LABEL maintainer="NaveenKumar Namachivayam"

WORKDIR /go/src/app

COPY . .

RUN go mod init

RUN go build  -o helloworld

EXPOSE 6111

CMD ["./helloworld"]

