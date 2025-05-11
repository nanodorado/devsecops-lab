resource "aws_s3_bucket" "insecure_bucket" {
  bucket = "example-public-bucket"
  acl    = "public-read"

  tags = {
    Name        = "Insecure Bucket"
    Environment = "Dev"
  }
}

resource "aws_security_group" "open_sg" {
  name        = "open-sg"
  description = "Security group with unrestricted ingress"
  vpc_id      = "vpc-12345678"

  ingress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}