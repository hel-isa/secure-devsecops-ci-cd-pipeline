terraform {
  required_version = ">= 1.6.0"
}

# Example only: secure defaults / placeholders.
# Prefer: remote state + state locking, RBAC, least privilege IAM, and secrets via a manager.

variable "environment" {
  type        = string
  description = "Environment name (dev/stage/prod)"
  default     = "dev"
}

output "note" {
  value = "Terraform example scaffold. Replace with real cloud resources."
}
