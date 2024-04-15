from prac_09.silver_service_taxi import SliverServiceTaxi


def main():
    silverservicetaxi = SliverServiceTaxi("My SilverServiceTaxi", 100, 2)
    silverservicetaxi.drive(33)
    print(silverservicetaxi)
    print(silverservicetaxi.get_fare())


main()