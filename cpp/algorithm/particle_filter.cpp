#include <iostream>
#include <vector>
#include <random>

struct Particle {
    double x;
    double y;
    double weight;
};

class ParticleFilter {
public:
    ParticleFilter(int numParticles) : numParticles(numParticles) {
        particles.resize(numParticles);
        weights.resize(numParticles);
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_real_distribution<double> dist(0.0, 1.0);
        for (int i = 0; i < numParticles; i++) {
            particles[i].x = dist(gen);
            particles[i].y = dist(gen);
            particles[i].weight = 1.0 / numParticles;
        }
    }

    void update(double deltaX, double deltaY) {
        std::random_device rd;
        std::mt19937 gen(rd());
        std::normal_distribution<double> dist(0.0, 0.1);
        for (int i = 0; i < numParticles; i++) {
            particles[i].x += deltaX + dist(gen);
            particles[i].y += deltaY + dist(gen);
        }
    }

    void resample() {
        std::random_device rd;
        std::mt19937 gen(rd());
        std::discrete_distribution<int> dist(weights.begin(), weights.end());
        std::vector<Particle> resampledParticles(numParticles);
        for (int i = 0; i < numParticles; i++) {
            int index = dist(gen);
            resampledParticles[i] = particles[index];
        }
        particles = resampledParticles;
    }

private:
    int numParticles;
    std::vector<Particle> particles;
    std::vector<double> weights;
};

int main() {
    ParticleFilter filter(100);
    filter.update(0.1, 0.2);
    filter.resample();
    return 0;
}
