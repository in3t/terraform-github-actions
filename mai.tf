resource "aws_instance" "web" {
  ami           = var.ami
  instance_type = var.instance_type
}

resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
  
  tags = {
    Name = "main-vpc"
  }
}