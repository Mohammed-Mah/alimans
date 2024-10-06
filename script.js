// Adjust the camera position to see in 3D perspective
camera.position.set(15, 15, 25); // Move the camera away and to the side
camera.lookAt(0, 0, 0); // Ensure camera is looking at the Sun

// Add orbiting in 3D by using Z-axis
function animate() {
    requestAnimationFrame(animate);

    // Get user inputs
    const semiMajorAxis = parseFloat(document.getElementById("semiMajorAxis").value);
    const eccentricity = parseFloat(document.getElementById("eccentricity").value);
    const periapsis = parseFloat(document.getElementById("periapsis").value) * (Math.PI / 180);

    // Animate planets' orbits
    planets.forEach((planetObj, index) => {
        const planet = planetObj.mesh;
        const distance = planetObj.distance * semiMajorAxis;
        const angle = time + (index * 45); // Angle is increased based on index

        // Calculate 3D positions
        const x = distance * Math.cos(angle) * (1 - eccentricity);
        const y = distance * Math.sin(angle) * (1 - eccentricity) * Math.cos(periapsis);
        const z = distance * Math.sin(angle) * Math.sin(periapsis); // Adding Z-axis movement

        planet.position.set(x, y, z); // Now planets move in 3D
    });

    time += 0.01; // Increment time for smooth animation
    renderer.render(scene, camera);
}