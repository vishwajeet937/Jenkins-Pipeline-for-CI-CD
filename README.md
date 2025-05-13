# Jenkins-Pipeline-for-CI-CD

## 🚀 Objective

The purpose of this project is to set up a basic Jenkins pipeline to automate the process of building and deploying a Docker-based application.

---

## 🛠️ Tools & Technologies

* **Jenkins** - For Continuous Integration and Deployment
* **Docker** - To containerize the application
* **Git** - Version Control System

---

## 📂 Project Structure

```
Jenkins-Pipeline-for-CI-CD/
├── Jenkinsfile                # Pipeline script
├── Dockerfile                 # Docker build configuration
├── app/                       # Application source code
│   └── index.js
├── README.md                  # Project documentation
└── .gitignore                 # Ignored files
```

---

## ⚙️ Jenkins Pipeline Stages

1️⃣ **Clone Repository:**

* Pulls the latest code from GitHub.

2️⃣ **Build Docker Image:**

* Builds a Docker image from the Dockerfile.

3️⃣ **Run Docker Container:**

* Deploys the application inside a Docker container.

4️⃣ **Post Actions:**

* Displays the application URL after successful deployment.

---

## 🚀 Jenkins Pipeline Configuration

1. Go to **Jenkins Dashboard → New Item → Pipeline**.
2. Name it: `MyApp-Pipeline`
3. In **Pipeline Definition**, select **Pipeline script from SCM**.
4. Add your Git repository URL.

---

## 🔄 GitHub Webhook Setup (Optional)

1. Navigate to your repository → **Settings → Webhooks**.
2. Add Payload URL: `http://<your-jenkins-server>:8080/github-webhook/`
3. Select **application/json** as content type.
4. Choose **Just the push event**.

---

## 📝 Usage

To trigger the pipeline, push any changes to the repository or click **Build Now** in Jenkins Dashboard.

---

## ✅ Verification

* Application should be accessible at:

```
http://localhost:8081
```

---

## 🔍 Improvements

* Add **Test Stage** for automated testing.
* Implement **Staging and Production** pipelines.
* Integrate **Docker Compose** for multi-container orchestration.

---

## 🤝 Contributing

Feel free to submit pull requests to improve the pipeline.

Developed by Vishwajeet Kumar
