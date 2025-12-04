from dataclasses import dataclass, field


class InvalidSizeBatch(Exception):
    """Ошибка. Выбрасывается, если batch_size <= 0."""

    pass


class InvalidDropout(Exception):
    """Ошибка. Выбрасывается, если dropout не удовлетворяет условию 0.0 <= dropout <= 1.0."""

    pass


class InvalidHiddenSizes(Exception):
    """Ошибка. Выбрасывается, если hidden_sizes пустой."""

    pass


class InvalidSeed(Exception):
    """Ошибка. Выбрасывается, если seed <= 0."""

    pass


@dataclass(slots=True)
class DatasetConfig:
    name: str
    path: str
    batch_size: int

    def __post_init__(self) -> None:
        if self.batch_size <= 0:
            raise InvalidSizeBatch(f'Параметр "batch_size={self.batch_size}" должен быть больше 0.')


@dataclass(frozen=True)
class ModelConfig:
    model_name: str
    hidden_sizes: list[int] = field(default_factory=list)
    dropout: float = 0.0

    def __post_init__(self) -> None:
        if not 0.0 <= self.dropout <= 1.0:
            raise InvalidDropout(
                f'Параметр "dropout={self.dropout}" не удовлетворяет условие 0.0 <= dropout <= 1.0.'
            )

        if not self.hidden_sizes:
            raise InvalidHiddenSizes(
                f'Параметр "hidden_sizes={self.hidden_sizes}" не может быть пустым.'
            )


@dataclass(slots=True)
class ExperimentConfig:
    name: str
    dataset: DatasetConfig
    model: ModelConfig
    seed: int = 42
    tags: list[str] = field(default_factory=list)
    created_by: str = "unknown"

    def __post_init__(self) -> None:
        self.name = self.name.strip()
        self.created_by = self.created_by.strip().lower()

        if self.seed <= 0:
            raise InvalidSeed(
                f'Параметр "seed={self.seed}" должен быть положительным числом (seed > 0).'
            )


@dataclass(order=True)
class ExperimentResult:
    config: ExperimentConfig = field(compare=False)
    metric: float
    duration_sec: float
    status: str = "ok"

    def __post_init__(self) -> None:
        self.metric = round(self.metric, 4)
        self.duration_sec = round(self.duration_sec, 4)


def main() -> None:
    # 1. Создаём несколько конфигов датасета
    imdb_dataset = DatasetConfig(
        name="IMDB Reviews",
        path="/data/imdb_reviews.csv",
        batch_size=32,
    )

    tweets_dataset = DatasetConfig(
        name="Tweets Sentiment",
        path="/data/tweets_sentiment.csv",
        batch_size=64,
    )

    # 2. Создаём несколько конфигов модели
    small_model = ModelConfig(
        model_name="small_mlp",
        hidden_sizes=[128, 64],
        dropout=0.1,
    )

    big_model = ModelConfig(
        model_name="big_transformer",
        hidden_sizes=[512, 512, 256],
        dropout=0.2,
    )

    # 3. Собираем конфиги экспериментов
    exp_imdb_small = ExperimentConfig(
        name="  imdb_small_exp_01  ",
        dataset=imdb_dataset,
        model=small_model,
        seed=42,
        tags=["baseline", "imdb"],
        created_by="Danil",
    )

    exp_imdb_big = ExperimentConfig(
        name="imdb_big_exp_01",
        dataset=imdb_dataset,
        model=big_model,
        seed=123,
        tags=["imdb", "transformer"],
        created_by="danil",
    )

    exp_tweets_small = ExperimentConfig(
        name="tweets_small_exp_01",
        dataset=tweets_dataset,
        model=small_model,
        seed=777,
        tags=["tweets", "baseline"],
        created_by="DataTeam",
    )

    # 4. Создаём результаты экспериментов
    results: list[ExperimentResult] = [
        ExperimentResult(
            config=exp_imdb_small,
            metric=0.87321,
            duration_sec=1234.56789,
            status="ok",
        ),
        ExperimentResult(
            config=exp_imdb_big,
            metric=0.91234,
            duration_sec=2100.12345,
            status="ok",
        ),
        ExperimentResult(
            config=exp_tweets_small,
            metric=0.84567,
            duration_sec=980.4321,
            status="ok",
        ),
    ]

    # 5. Печатаем все результаты как есть
    print("=== Все результаты экспериментов ===")
    for r in results:
        print(r)

    # 6. Сортируем результаты по метрике (от лучшего к худшему)
    sorted_results = sorted(results, reverse=True)

    print("\n=== Отсортировано по метрике (лучшие сверху) ===")
    for r in sorted_results:
        print(f"metric={r.metric:.4f}, duration={r.duration_sec:.2f}, name={r.config.name}")

    # 7. Покажем лучший и худший эксперимент отдельно
    best = max(results)
    worst = min(results)

    print("\n=== Лучший эксперимент ===")
    print(f"metric={best.metric:.4f}, duration={best.duration_sec:.2f}, name={best.config.name}")

    print("\n=== Худший эксперимент ===")
    print(f"metric={worst.metric:.4f}, duration={worst.duration_sec:.2f}, name={worst.config.name}")


if __name__ == "__main__":
    main()
