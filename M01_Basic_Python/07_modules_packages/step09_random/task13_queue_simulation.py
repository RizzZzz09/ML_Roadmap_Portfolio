import random


def main():
    n = 10_000
    interval = 1.0
    random.seed(123)

    # Абсолютное время приходов
    arrivals = []
    t = 0.0
    for _ in range(n):
        t += random.expovariate(interval)
        arrivals.append(t)

    mu = 0.8
    sigma = 0.1

    # Время обслуживания
    service_times = []
    for _ in range(n):
        s = random.gauss(mu, sigma)
        if s < 0.01:
            s = 0.01
        service_times.append(s)

    # Метрики
    wait_times = []
    queue_lengths = []

    # Список концов обслуживания в порядке возрастания
    end_times = []
    front = 0

    for i in range(n):
        arrival = arrivals[i]
        s_time = service_times[i]

        # 1) удаляем всех, кто уже завершился к моменту arrival
        while front < len(end_times) and end_times[front] <= arrival:
            front += 1

        in_system = len(end_times) - front
        queue_len = max(0, in_system - 1)

        # 2) вычисляем момент старта обслуживания
        if in_system == 0:
            start = arrival
        else:
            start = end_times[-1]

        wait = start - arrival
        end = start + s_time

        # 3) записываем метрики и планируем завершение
        wait_times.append(wait)
        queue_lengths.append(queue_len)
        end_times.append(end)

    # Итоги
    avg_wait = sum(wait_times) / n
    avg_service = sum(service_times) / n
    avg_queue = sum(queue_lengths) / n

    print(f"Average wait time: {avg_wait:.3f}")
    print(f"Average service time: {avg_service:.3f}")
    print(f"Average queue length: {avg_queue:.3f}")


if __name__ == "__main__":
    main()
