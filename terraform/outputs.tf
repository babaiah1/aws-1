output "ecr_repo" {
  value = aws_ecr_repository.app.repository_url
}
output "alb_dns" {
  value = aws_lb.alb.dns_name
}
