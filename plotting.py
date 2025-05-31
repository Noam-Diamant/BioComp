from typing import List
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np


class ExecutionTimeAnalyzer:
    def __init__(self, log_path: str):
        self.log_path = log_path
        self.execution_times = []
        self._read_times()
    
    def _read_times(self) -> None:
        """Extract execution times from log file"""
        with open(self.log_path, 'r') as log:
            self.execution_times = [
                float(line.split()[2])
                for line in log
                if line.startswith('Execution time:')
            ]
            print("Found times:", self.execution_times)
    
    @staticmethod
    def _fitting_function(x: float, scale: float, growth: float) -> float:
        """Double exponential growth function"""
        return scale * np.power(2, np.power(2, growth * x))
    
    def create_plot(self, output_path: str = './execution_times.png') -> None:
        """Generate and save execution time plot"""
        # Prepare data
        sizes = np.arange(1, len(self.execution_times) + 1)
        times = np.array(self.execution_times)
        
        # Create figure
        plt.figure(figsize=(10, 6))
        
        # Plot actual data points
        plt.scatter(sizes, times, 
                   color='blue', 
                   label='Measured Times',
                   marker='o')
        
        # Fit curve and plot
        params, _ = curve_fit(self._fitting_function, sizes, times)
        fitted_curve = self._fitting_function(sizes, *params)
        plt.plot(sizes, fitted_curve,
                color='red',
                label=f'Fit: {params[0]:.5f}*2^(2^({params[1]:.5f}*size))')
        
        # Customize plot
        plt.xlabel('Graph Size (n)')
        plt.ylabel('Execution Time (seconds)')
        plt.title('Execution Times')
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()
        
        # Save and display
        plt.savefig(output_path)
        plt.show()


def main():
    analyzer = ExecutionTimeAnalyzer('./graphs.txt')
    analyzer.create_plot()


if __name__ == '__main__':
    main()