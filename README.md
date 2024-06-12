# ontap-custom-metrics
Custom NetApp ONTAP metrics collector in Ansible (to close Harvest gaps)

What is does:
- Ansible playbooks collect data from ONTAP
- Auth data is collected from locally running NetApp Harvest (cert and/or basic)
- Formats data for Prometheus database (jinja templates)
- Sends metrocs to Prometheus Pushgateway

TODO:
- Contenerize
- Read auth data from remote Harvest instance