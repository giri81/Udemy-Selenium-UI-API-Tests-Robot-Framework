class GitHubAPIUtils:
    """
    A utility class for GitHub API related operations.
    """

    @staticmethod
    def create_repo_url(owner, repo_name):
        """
        Construct the URL for a GitHub repository based on the owner and repository name.

        :param owner: The owner of the GitHub repository.
        :type owner: str
        :param repo_name: The name of the GitHub repository.
        :type repo_name: str
        :return: The URL for the GitHub repository.
        :rtype: str
        """
        return f'https://api.github.com/repos/{owner}/{repo_name}'
