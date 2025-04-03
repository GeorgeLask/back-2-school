import hydra
from omegaconf import DictConfig
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


@hydra.main(config_path="conf", config_name="config", version_base=None)
def train(cfg: DictConfig):
    print(f"Running experiment with configuration:\n{cfg}")

    # Load dataset
    if cfg.dataset.name == "iris":
        data = datasets.load_iris()
    else:
        raise ValueError("Unsupported dataset")


    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=cfg.train.test_size, random_state=cfg.train.random_state
    )

    # Load model based on configuration
    if cfg.model.name == "random_forest":
        model = RandomForestClassifier(
        n_estimators=cfg.model.n_estimators,
        max_depth=cfg.model.max_depth,
        random_state=cfg.model.random_state
    )
    elif cfg.model.name == "logistic_regression":
        model = LogisticRegression(
            C=cfg.model.C, max_iter=cfg.model.max_iter, random_state=cfg.model.random_state
        )
    else:
        raise ValueError("Unsupported model")

    # Train and evaluate
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.4f}")

if __name__ == "__main__":
    train()