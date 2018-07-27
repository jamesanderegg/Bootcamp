-- 1a. Display the first and last names of all actors from the table `actor`.
SELECT a.first_name, a.last_name 
FROM actor a;

-- 1b. COMBINE
SELECT a.first_name, a.last_name,CONCAT(a.first_name," ", a.last_name) 
FROM actor a;

-- 2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe." What is one query would you use to obtain this information?
SELECT a.first_name, a.last_name,CONCAT(a.first_name," ", a.last_name) 
FROM actor a
WHERE a.first_name LIKE 'Joe';
-- 2b. Find all actors whose last name contain the letters `GEN`:
SELECT a.first_name, a.last_name,CONCAT(a.first_name," ", a.last_name) 
FROM actor a
WHERE a.last_name LIKE '%GEN%';

-- 2c. Find all actors whose last names contain the letters `LI`. This time, order the rows by last name and first name, in that order:
SELECT a.first_name, a.last_name,CONCAT(a.first_name," ", a.last_name) 
FROM actor a
WHERE a.last_name LIKE '%LI%'
order by a.first_name, a.last_name;

-- 2d. Using `IN`, display the `country_id` and `country` columns of the following countries: Afghanistan, Bangladesh, and China:
SELECT c.country_id, c.country 
FROM COUNTRY as c
WHERE c.country IN('Afghanistan', 'Bangladesh','China');

-- 3a. Add a `middle_name` column to the table `actor`. Position it between `first_name` and `last_name`. Hint: you will need to specify the data type.
ALTER TABLE actor
ADD COLUMN middle_name VARCHAR(15) AFTER first_name;

-- 3b. You realize that some of these actors have tremendously long last names. Change the data type of the `middle_name` column to `blobs`.
ALTER TABLE actor Change middle_name blobs VARCHAR(15);

-- 3c. Now delete the `middle_name` column.
ALTER TABLE actor DROP COLUMN blobs;

-- 4a. List the last names of actors, as well as how many actors have that last name.

SELECT a.last_name, Count(*) as how_many_actors
FROM actor as a
GROUP BY 1;

-- 4b. List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors

SELECT a.last_name, Count(*) as count_actors
FROM actor as a
GROUP BY 1
HAVING COUNT(*) >= 2;

-- 4c. Oh, no! The actor `HARPO WILLIAMS` was accidentally entered in the `actor` table as `GROUCHO WILLIAMS`, 
-- the name of Harpo's second cousin's husband's yoga teacher. Write a query to fix the record.

UPDATE actor
SET first_name = REPLACE(first_name, 'GROUCHO', 'HARPO')
WHERE first_name LIKE ('GROUCHO') AND last_name LIKE ('WILLIAMS');

SELECT *
FROM actor;

-- 4d. Perhaps we were too hasty in changing `GROUCHO` to `HARPO`. It turns out that `GROUCHO` was the correct name after all! In a single query, 
-- if the first name of the actor is currently `HARPO`, change it to `GROUCHO`. Otherwise, change the first name to `MUCHO GROUCHO`, as that is 
-- exactly what the actor will be with the grievous error. BE CAREFUL NOT TO CHANGE THE FIRST NAME OF EVERY ACTOR TO `MUCHO GROUCHO`,
-- HOWEVER! (Hint: update the record using a unique identifier.)
UPDATE actor
SET first_name = 
			CASE
				WHEN first_name = 'HARPO' THEN 'GROUCHO'
            END
WHERE first_name IN ('HARPO');

SELECT * 
from actor;

-- 5a. You cannot locate the schema of the `address` table. Which query would you use to re-create it?

SHOW CREATE TABLE address;

--  * Hint: <https://dev.mysql.com/doc/refman/5.7/en/show-create-table.html>

-- 6a. Use `JOIN` to display the first and last names, as well as the address, of each staff member. Use the tables `staff` and `address`:
SELECT staff.first_name, staff.last_name, address.address, address.district, address.city_id, address.postal_code
FROM staff
INNER JOIN address on address.address_id = staff.address_id;

-- 6b. Use `JOIN` to display the total amount rung up by each staff member in August of 2005. Use tables `staff` and `payment`. 
select staff.username, p.staff_id, sum(p.amount) as total_amount, p.payment_date as first_payment
from payment p
	JOIN staff on p.staff_id = staff.staff_id
where p.payment_date > '2005-08-01'
group by staff.username;

-- 6c. List each film and the number of actors who are listed for that film. Use tables `film_actor` and `film`. Use inner join.
SELECT *
from film_actor;

SELECT f.film_id, f.title, film_actor.actor_id
FROM film as f
	INNER JOIN film_actor on f.film_id = film_actor.film_id
;
-- ????????????????????????????????????? NEED TO GROUP BY HAND CONCAT ACTOR ID

-- 6d. How many copies of the film `Hunchback Impossible` exist in the inventory system?
SELECT * 
FROM FILM;

select film.title, Count(title)
FROM inventory
Join film on inventory.film_id = film.film_id
WHERE title LIKE 'HUNCHBACK IMPOSSIBLE'
GROUP BY film.title;

-- 6e. Using the tables `payment` and `customer` and the `JOIN` command, list the total paid by each customer. List the customers alphabetically by last name:
SELECT p.customer_id, c.first_name, c.last_name,SUM(p.amount)
FROM payment p
JOIN customer c on c.customer_id = p.customer_id
GROUP BY c.first_name, p.customer_id;

-- 7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an unintended consequence, 
-- films starting with the letters `K` and `Q` have also soared in popularity. 
-- Use subqueries to display the titles of movies starting with the letters `K` and `Q` whose language is English.
SELECT f2.title, f2.language_id
	FROM film f2 
    WHERE f2.title LIKE 'k%' OR f2.title LIKE 'q%'
    AND f2.film_id IN (
		SELECT f.film_id
		FROM film f 
			JOIN language l ON l.language_id = f.language_id
		WHERE l.name = 'English'
);

-- 7b. Use subqueries to display all actors who appear in the film `Alone Trip`.
SELECT a.first_name, a. last_name
FROM actor as a
WHERE actor_id IN (
	SELECT actor_id
    FROM film_actor as fa
    WHERE film_id IN 
    (
    SELECT film_id
    FROM film as f
    WHERE title LIKE 'ALONE TRIP'
		)
    );

-- 7c. You want to run an email marketing campaign in Canada, for which you will need the names and email addresses of all Canadian customers.
-- Use joins to retrieve this information.

SELECT c.first_name, c.last_name, country.country
FROM customer as c
JOIN address as a ON a.address_id = c.customer_id
JOIN city as city ON city.city_id = a.address_id
JOIN country as country ON country.country_id = city.country_id
WHERE country.country LIKE 'CANADA';

-- 7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. 
-- Identify all movies categorized as family films.
SELECT f.*, c.name, f1.title
FROM film_category as f
JOIN film as f1 ON f1.film_id = f.film_id
JOIN category as c ON c.category_id = f.category_id
WHERE c.name LIKE 'FAMILY' OR c.name LIKE 'CHILDREN';

-- 7e. Display the most frequently rented movies in descending order.
SELECT r.inventory_id, COUNT(r.inventory_id) AS Frequency, i.film_id, f.title
FROM rental as r
JOIN inventory as I ON i.inventory_id = r.inventory_id
JOIN film as f ON f.film_id = i.film_id
GROUP BY r.inventory_id
ORDER BY (Frequency) DESC;

-- 7f. Write a query to display how much business, in dollars, each store brought in.
select staff.username, p.staff_id, sum(p.amount) as total_amount, p.payment_date as first_payment
from payment p
	JOIN staff on p.staff_id = staff.staff_id
group by staff.username;

-- 7g. Write a query to display for each store its store ID, city, and country.
SELECT s.store_id, s.address_id, a.address, a.city_id, c.city, c.country_id, cy.country
FROM store as s
JOIN address as a ON s.address_id = a.address_id
JOIN city as c ON a.city_id = c.city_id
JOIN country as cy ON c.country_id = cy.country_id;

-- 7h. List the top five genres in gross revenue in descending order. 
-- (**Hint**: you may need to use the following tables: category, film_category, inventory, payment, and rental.)
SELECT SUM(p.amount), c.name
FROM rental r
JOIN payment p ON p.rental_id = r.rental_id
JOIN inventory i on i.inventory_id = r.inventory_id
JOIN film_category f ON f.film_id = i.film_id
JOIN category c ON c.category_id = f.category_id
GROUP BY c.name
ORDER BY SUM(p.amount) DESC Limit 5;

-- 8a. In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. 
-- Use the solution from the problem above to create a view. If you haven't solved 7h, you can substitute another query to create a view.
CREATE VIEW `TOP_5_GROSSING` AS 
SELECT SUM(p.amount), c.name
FROM rental r
JOIN payment p ON p.rental_id = r.rental_id
JOIN inventory i on i.inventory_id = r.inventory_id
JOIN film_category f ON f.film_id = i.film_id
JOIN category c ON c.category_id = f.category_id
GROUP BY c.name
ORDER BY SUM(p.amount) DESC Limit 5;

-- 8b. How would you display the view that you created in 8a?
SELECT *
FROM top_5_grossing;

-- 8c. You find that you no longer need the view `top_five_genres`. Write a query to delete it.
DROP VIEW top_5_grossing;