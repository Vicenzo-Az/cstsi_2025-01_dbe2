# api/management/commands/seed.py
from django.core.management.base import BaseCommand
from django.core.management import call_command
from api.factories import (
    UserFactory,
    DataSourceFactory,
    DashboardFactory,
    AnalysisReportFactory,
)


class Command(BaseCommand):
    help = 'Popula o banco com dados de teste usando factories e aplica migrations automaticamente'

    def add_arguments(self, parser):
        parser.add_argument(
            '--users',
            type=int,
            default=5,
            help='Número de usuários a serem criados'
        )
        parser.add_argument(
            '--datasources-per-user',
            type=int,
            default=3,
            help='Número de DataSources por usuário'
        )
        parser.add_argument(
            '--dashboards-per-user',
            type=int,
            default=2,
            help='Número de Dashboards por usuário'
        )
        parser.add_argument(
            '--reports-per-user',
            type=int,
            default=1,
            help='Número de AnalysisReports por usuário'
        )

    def handle(self, *args, **options):
        # Aplica migrations antes do seed
        self.stdout.write(self.style.NOTICE('Aplicando migrations...'))
        call_command('migrate', verbosity=0, interactive=False)

        total_users = options['users']
        ds_per = options['datasources_per_user']
        db_per = options['dashboards_per_user']
        rp_per = options['reports_per_user']

        self.stdout.write(self.style.MIGRATE_HEADING(
            f"Iniciando seed: {total_users} usuários"))
        for _ in range(total_users):
            user = UserFactory()
            self.stdout.write(self.style.SUCCESS(
                f"Usuário criado: {user.username}"))

            # DataSources
            ds_list = DataSourceFactory.create_batch(ds_per, user=user)
            self.stdout.write(self.style.SUCCESS(
                f"  {len(ds_list)} DataSources criados para {user.username}"
            ))

            # Dashboards
            for _ in range(db_per):
                dash = DashboardFactory(user=user, data_sources=ds_list)
                self.stdout.write(self.style.SUCCESS(
                    f"  Dashboard criado: {dash.name}"
                ))

            # AnalysisReports
            for _ in range(rp_per):
                rpt = AnalysisReportFactory(user=user, data_sources=ds_list)
                self.stdout.write(self.style.SUCCESS(
                    f"  AnalysisReport criado: {rpt.title[:30]}..."
                ))

        self.stdout.write(self.style.MIGRATE_LABEL(
            "Seed concluído com sucesso!"))
