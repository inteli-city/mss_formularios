import pytest
from src.shared.infra.repositories.profile_repository_dynamo import ProfileRepositoryDynamo


class Test_ProfileRepositoryDynamo:

    @pytest.mark.skip("Can't test it locally")
    def test_profile_repository_dynamo_update_profile(self):
        repo = ProfileRepositoryDynamo()

        repo.update_profile(
            profile_id='125fb34e-aacf-4a47-9914-82ea64ff9f32',
            systems_to_include=['JUNDIAI'])
        

        assert 1 == 0