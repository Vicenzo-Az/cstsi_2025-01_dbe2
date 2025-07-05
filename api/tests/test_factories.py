import pytest
from api.factories import UserFactory, DashboardFactory, DataSourceFactory


@pytest.mark.django_db
def test_user_factory_creates_user():
    user = UserFactory()
    assert user.pk is not None
    assert user.username


@pytest.mark.django_db
def test_dashboard_has_data_sources():
    dash = DashboardFactory()
    # por padrão geramos 2 data_sources
    assert dash.data_sources.count() == 2


@pytest.mark.django_db
def test_custom_data_sources_extraction():
    from api.factories import DataSourceFactory
    ds_list = DataSourceFactory.create_batch(5)
    dash = DashboardFactory(data_sources=ds_list)
    assert dash.data_sources.count() == 5
