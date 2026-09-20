variable "ami" {
  description = "The AMI to use for the instance"
  type        = string
  default     = "ami-01a00762f46d584a1"
}

variable "instance_type" {
  description = "The instance type to use for the instance"
  type        = string
  default     = "t2.micro"
}