import numpy as np

def particle_filter(num_particles, motion_model, measurement_model, initial_state, measurements):
    # Initialize particles
    particles = np.random.rand(num_particles, 2)  # Assuming 2D state space
    
    for measurement in measurements:
        # Motion update
        particles = motion_model(particles)
        
        # Measurement update
        weights = measurement_model(particles, measurement)
        weights /= np.sum(weights)  # Normalize weights
        
        # Resampling
        indices = np.random.choice(np.arange(num_particles), size=num_particles, replace=True, p=weights)
        particles = particles[indices]
    
    # Estimate the final state
    estimated_state = np.mean(particles, axis=0)
    
    return estimated_state
