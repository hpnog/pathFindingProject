from multiprocessing import Process


class Dijkstra(Process):
    def run(self) -> None:
        for _ in range(10):
            print("Running here my friends ")

