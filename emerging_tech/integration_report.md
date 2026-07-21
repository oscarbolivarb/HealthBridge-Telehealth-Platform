# Integration Report

## Emerging Technology: GitHub Actions (CI/CD)

## Evaluation 

From the beginning, the HealthBridge project has been developed using GitHub, so GitHub Actions was selected because it works directly with GitHub. There are other tools such as CircleCI and Jenkins that are similar but GitHub Actions was the easiest to set up and it did not require an additional account.

The main reason for using this tool was to be able to automate part of the development process, instead of doing everything manually. GitHub Actions can automatically run a workflow every time a change is made and it can be pushed to the repository.

This also helps finding problems earlier, keeps the project organized and it is easier to maintain; especially if there new features are going to be added in the future.

## Integration 

GitHub Actions was used to create a workflow that runs automatically whenever there are changes pushed to the repository. After the workflow files were created, it was added to GitHub and tested to make sure that it worked correctly. 

The following tasks were completed:

- GitHub Actions workflow was created.
- The workflow was configured to run automatically.
- The workflow was tested to make sure it ran successfully.
- The integration report was added to the repository. 

The evidence includes:

- A screenshot showing the GitHub Actions workflow completed successfully.
- Git commit showing that the GitHub Actions workflow was added.
- Git commit showing that the integration report was added.
- 

<img width="3427" height="812" alt="image" src="https://github.com/user-attachments/assets/6483bdf5-8bd7-4bfa-b537-2b0df1d0a0e1" />



One benefit of GitHub Actions is that it saves time because some tasks were completed automatically, it also helped reduce mistakes that happen when it is done manually. One challenge was learning how to create a workflow using a YAML file.

## Ethical Reflection

An ethical concern regarding GitHub Actions is being able to protect sensitive information, since the healthcare platform has patient’s information that should not be included in the workflow files or logs. At the same time, any passwords or API keys should be stored using GitHub Secrets instead of being written in the code directly. 

Another concern is vendor lock-in, since GitHub Actions only works with GitHub. So if the project is moved to another platform, then it would require creating a new automation process. By keeping the workflow simple and documented it makes it easier to work on it in the future.

Overall, the project has improved by automating some tasks using GitHub Actions and the workflow is more organized.
