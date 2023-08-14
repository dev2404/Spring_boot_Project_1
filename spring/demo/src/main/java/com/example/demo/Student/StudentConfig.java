package com.example.demo.Student;

import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.time.LocalDate;
import java.time.Month;
import java.util.List;

@Configuration
public class StudentConfig {

    @Bean
    CommandLineRunner commandLineRunner(StudentRepository repository) {
        return args -> {
            Student devi =  new Student(
                    "devilal",
                    "devilal@gmail.com",
                    LocalDate.of(2000, Month.AUGUST,21));

            Student Ram =  new Student(
                    "Ram",
                    "Ramlal@gmail.com",
                    LocalDate.of(2005, Month.AUGUST,21));

            repository.saveAll(List.of(devi, Ram));

        };
    }
}
