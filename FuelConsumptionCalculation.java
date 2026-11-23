class SimpleCar {
    private String maker; // Honda Toyota, Nissan, etc.
    private int distance = 0; // distance travelled
    private float fuelEconomy; // Table 2, Column 2

    public SimpleCar(String maker, float fuelEconomy) {
        this.maker = maker;
        this.fuelEconomy = fuelEconomy;
    }

    public void setData(int distance) {
        this.distance = distance;
    }

    public String getMaker() { return maker; }
    public int getDistance() { return distance; }
    public float getFuelEconomy() { return fuelEconomy; }

    public float calculateFuelConsumptionOldRegulations() {
        return distance / fuelEconomy;
    }

    public float calculateFuelConsumptionNewRegulations() {
        float r = calculateFuelConsumptionOldRegulations();
        return r;
    }
}

class AdvancedCar extends SimpleCar {
    private float acFuel; // Tab 2, Column 3
    private int beginWork = 0; // time to begin work
    private int endWork = 0; // time to end work

    public AdvancedCar(String maker, float fuelEconomy, float acFuel) {
        super(maker, fuelEconomy);
        this.acFuel = acFuel;
    }

    public void setData(int beginWork, int endWork, int distance) {
        super.setData(distance);
        this.beginWork = beginWork;
        this.endWork = endWork;
    }

    public float getAcFuel() { return acFuel; }

    @Override
    public float calculateFuelConsumptionOldRegulations() {
        float r = super.calculateFuelConsumptionOldRegulations() + (endWork - beginWork) / acFuel;
        return r;
    }

    @Override
    public float calculateFuelConsumptionNewRegulations() {
        float r = calculateFuelConsumptionOldRegulations();
        return r;
    }
}

class DeluxeCar extends AdvancedCar {
    private int timeWithPassengers = 0;

    public DeluxeCar(String maker, float fuelEconomy, float acFuel) {
        super(maker, fuelEconomy, acFuel);
    }

    public void setData(int beginWork, int endWork, int distance, int timeWithPassengers) {
        super.setData(beginWork, endWork, distance);
        this.timeWithPassengers = timeWithPassengers;
    }

    @Override
    public float calculateFuelConsumptionOldRegulations() {
        float r = super.calculateFuelConsumptionOldRegulations();
        return r;
    }

    @Override
    public float calculateFuelConsumptionNewRegulations() {
        return getDistance() / getFuelEconomy() + (float) timeWithPassengers / getAcFuel();
    }
}

public class FuelConsumptionCalculation {

    private double fuelConsumptionOldRegulation = 0;
    private double fuelConsumptionNewRegulation = 0;
    private SimpleCar[] cars;

    public FuelConsumptionCalculation() {
        final int MAX_CARS = 4;
        cars = new SimpleCar[MAX_CARS];
        cars[0] = new DeluxeCar("Honda", 14f, 10.5f);
        ((DeluxeCar)cars[0]).setData(7, 18, 300, 10);
        cars[1] = new AdvancedCar("Toyota", 15.5f, 9.5f);
        ((AdvancedCar)cars[1]).setData(7, 18, 200);
        cars[2] = new SimpleCar("Nissan", 13.0f);
        cars[2].setData(350);
        cars[3] = new DeluxeCar("Van (Nissan)", 10.5f, 6f);
        ((DeluxeCar)cars[3]).setData(7, 18, 400, 7);
        calculateFuelConsumption();
    }

    public FuelConsumptionCalculation(SimpleCar[] cars) {
        this.cars = cars;
        calculateFuelConsumption();
    }

    private void calculateFuelConsumption() {
        fuelConsumptionOldRegulation = 0;
        fuelConsumptionNewRegulation = 0;
        for (int i = 0; i < cars.length; i++) {
            fuelConsumptionOldRegulation += cars[i].calculateFuelConsumptionOldRegulations();
            fuelConsumptionNewRegulation += cars[i].calculateFuelConsumptionNewRegulations();
        }
    }


    public double getFuelConsumptionOldRegulation() {
        return fuelConsumptionOldRegulation;
    }

    public double getFuelConsumptionNewRegulation() {
        return fuelConsumptionNewRegulation;
    }

    public static void main(String[] args) {
        System.out.println("--- Fleet Fuel Consumption Report ---");
        FuelConsumptionCalculation calculation = new FuelConsumptionCalculation();

        System.out.printf("Total Fuel Consumption (Old Regulation): %.2f\n", calculation.getFuelConsumptionOldRegulation());
        System.out.printf("Total Fuel Consumption (New Regulation): %.2f\n", calculation.getFuelConsumptionNewRegulation());

        
        double fuelSaved = calculation.getFuelConsumptionOldRegulation() - calculation.getFuelConsumptionNewRegulation();
        System.out.printf("Amount of Fuel Saved: %.2f\n", fuelSaved);
    }
}