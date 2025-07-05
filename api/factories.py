# api/factories.py
import factory
from factory.declarations import LazyAttribute, LazyFunction, SubFactory, Iterator, PostGenerationMethodCall
from factory.helpers import post_generation
from django.contrib.auth import get_user_model
from faker import Faker

from api.models import DataSource, Dashboard, AnalysisReport

fake = Faker()
User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        skip_postgeneration_save = True

    username = LazyAttribute(lambda _: fake.user_name())
    email = LazyAttribute(lambda _: fake.email())
    password = PostGenerationMethodCall('set_password', 'password123')


class DataSourceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = DataSource
        skip_postgeneration_save = True

    user = SubFactory(UserFactory)
    name = LazyAttribute(lambda _: fake.word().capitalize())
    source_type = Iterator([choice[0] for choice in DataSource.SOURCE_TYPES])
    connection_details = LazyFunction(
        lambda: {'url': fake.url(), 'api_key': fake.uuid4()})
    created_at = LazyFunction(lambda: fake.date_time_this_year())


class DashboardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Dashboard
        skip_postgeneration_save = True

    user = SubFactory(UserFactory)
    name = LazyAttribute(lambda _: fake.word().capitalize())
    description = LazyAttribute(lambda _: fake.sentence())
    config = LazyFunction(lambda: {'layout': 'grid', 'theme': fake.word()})
    created_at = LazyFunction(lambda: fake.date_time_this_year())

    @post_generation
    def data_sources(self, create, extracted, **kwargs):
        if not create:
            return
        items = extracted if extracted else [
            DataSourceFactory() for _ in range(2)]
        for ds in items:
            self.data_sources.add(ds)  # type: ignore


class AnalysisReportFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AnalysisReport
        skip_postgeneration_save = True

    user = SubFactory(UserFactory)
    title = LazyAttribute(lambda _: fake.sentence(nb_words=6))
    content = LazyAttribute(lambda _: fake.paragraph(nb_sentences=3))
    generated_by_ai = LazyAttribute(
        lambda _: fake.boolean(chance_of_getting_true=30))
    created_at = LazyFunction(lambda: fake.date_time_this_year())

    @post_generation
    def data_sources(self, create, extracted, **kwargs):
        if not create:
            return
        items = extracted if extracted else [
            DataSourceFactory() for _ in range(3)]
        for ds in items:
            self.data_sources.add(ds)  # type: ignore
