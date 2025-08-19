/**
 * Defines the public contract for a date range.
 * Any object that has these properties can be treated as a DateRange.
 */
interface IDateRange {
    readonly startDate: Date;
    readonly endDate: Date;
    readonly dates: Date[];
}

class DateRange implements IDateRange {
    // Private property to cache the calculated dates.
    private _dates?: Date[];

    constructor(
        public readonly startDate: Date,
        public readonly endDate: Date) {}

    /**
     * Returns an array with all the dates from startDate to endDate.
     * The result is calculated on the first access and cached for subsequent calls.
     */
    get dates(): Date[] {
        // If the dates have already been calculated, return the cached version.
        if (this._dates) {
            return this._dates;
        }

        // Otherwise, calculate them for the first time.
        const dateList: Date[] = [];
        const currentDate = new Date(this.startDate);
        while (currentDate <= this.endDate) {
            dateList.push(new Date(currentDate));
            currentDate.setDate(currentDate.getDate() + 1);
        }

        // Cache the result and return it.
        this._dates = dateList;
        return this._dates;
    }
}

class Employee {
    // The constructor for DateRange requires two arguments.
    // Example: a vacation for the next 7 days starting from today.
    vacations: DateRange[]
    leaveDaysRemaining?: number;
    
    constructor() {
        this.vacations = [];
    }
}

const employee = new Employee();
employee.vacations.push(new DateRange(new Date(), new Date(new Date().setDate(new Date().getDate() + 7))));
console.log(employee);
