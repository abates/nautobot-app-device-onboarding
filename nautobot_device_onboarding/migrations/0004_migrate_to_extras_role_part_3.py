from django.db import connection, migrations


class Migration(migrations.Migration):
    dependencies = [
        ("nautobot_device_onboarding", "0004_migrate_to_extras_role_part_2"),
    ]

    nautobot_run_before = [
        ("dcim", "0031_remove_device_role_and_rack_role"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="onboardingtask",
            name="role",
        ),
        migrations.RenameField(
            model_name="onboardingtask",
            old_name="new_role",
            new_name="role",
        ),
    ]

    def __init__(self, name, app_label):
        super().__init__(name, app_label)
        if self.nautobot_run_before:
            recorder = migrations.recorder.MigrationRecorder(connection)
            applied_migrations = recorder.applied_migrations()
            if ("nautobot_device_onboarding", "0001_initial") in applied_migrations:
                for migration in self.nautobot_run_before:
                    if migration not in applied_migrations:
                        self.run_before.append(migration)
