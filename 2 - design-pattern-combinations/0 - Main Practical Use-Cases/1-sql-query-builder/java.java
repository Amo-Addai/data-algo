
import java.util.ArrayList;
import java.util.List;
import java.util.function.Supplier;

// import org.springframework.jdbc.core.JdbcTemplate;
// import org.springframework.stereotype.Component;
// import org.springframework.beans.factory.annotation.Autowired;
// import org.springframework.stereotype.Service;


public class java {

    public static void main(String[] args) {
        Main.main(args);
    }

    public void tests() {
        // TODO: Write more tests
    }

    public static class Main {

        /*

        Here's a SQLQueryBuilder class that follows the Builder pattern,
        allowing you to construct SQL queries in a step-by-step manner.
        It supports building SELECT, INSERT, UPDATE, and DELETE queries,
        as well as additional SQL clauses like JOIN, ORDER BY, LIMIT, and WHERE.

        This example focuses on modularity, making it flexible for various SQL query types:

        Explanation of the SQLQueryBuilder Methods

        select(): Begins a SELECT query with specified columns.
        insertInto(): Begins an INSERT query with specified table and columns.
        update(): Begins an UPDATE query for a specified table.
        deleteFrom(): Begins a DELETE query from a specified table.
        columns(): Adds column arguments for an INSERT or SELECT query.
        values(): Adds values to be inserted in an INSERT query.
        set(): Sets column-value pairs for an UPDATE query.
        where(): Adds a WHERE clause to filter results.
        join(): Adds JOIN clauses with the specified table and condition.
        orderBy(): Adds ORDER BY clause to sort results.
        limit(): Limits the number of results in SELECT.

        This pattern allows chaining of methods to build up various types of SQL queries in a modular and readable way.

         */

        public static class SQLQueryBuilder {

            private String queryType;
            private StringBuilder query;

            private SQLQueryBuilder() {
                this.query = new StringBuilder();
            }

            // Entry point for builder pattern
            public static SQLQueryBuilder create() {
                return new SQLQueryBuilder();
            }

            // Base command methods - SELECT, INSERT, UPDATE, DELETE
            public SQLQueryBuilder select(String... columns) {
                queryType = "SELECT";
                query.append("SELECT ")
                        .append(String.join(", ", columns))
                        .append(" ");
                return this;
            }

            public SQLQueryBuilder insertInto(String table, String... columns) {
                queryType = "INSERT";
                query.append("INSERT INTO ")
                        .append(table)
                        .append(" (")
                        .append(String.join(", ", columns))
                        .append(") ");
                return this;
            }

            public SQLQueryBuilder update(String table) {
                queryType = "UPDATE";
                query.append("UPDATE ")
                        .append(table)
                        .append(" SET ");
                return this;
            }

            public SQLQueryBuilder deleteFrom(String table) {
                queryType = "DELETE";
                query.append("DELETE FROM ")
                        .append(table)
                        .append(" ");
                return this;
            }

            // Add column arguments & values

            public SQLQueryBuilder columns(String... columns) {
                if (queryType.equals("INSERT"))
                    query.append("(")
                            .append(String.join(", ", columns))
                            .append(") ");
                else if (queryType.equals("SELECT"))
                    // offset 7 letters for: "SELECT "
                    query.insert(7, String.join(", ", columns) + " ");
                return this;
            }

            public SQLQueryBuilder values(Object... values) {
                if (queryType.equals("INSERT")) {
                    query.append("VALUES (");
                    for (int i = 0; i < values.length; i++) {
                        query.append("?");
                        if (i < values.length - 1)
                            query.append(", ");
                    }
                    query.append(") ");
                }
                return this;
            }

            public SQLQueryBuilder set(String column, Object value) {
                if (queryType.equals("UPDATE"))
                    if (query.toString().endsWith("SET "))
                        query.append(column)
                                .append(" = ?");
                    else
                        query.append(", ")
                                .append(column)
                                .append(" = ?");
                return this;
            }

            // Additional clauses - FROM, WHERE, JOIN, ..

            public SQLQueryBuilder from(String table) {
                query.append(" FROM ")
                        .append(table);
                return this;
            }

            public SQLQueryBuilder where(String condition) {
                query.append(" WHERE ")
                        .append(condition);
                return this;
            }

            public SQLQueryBuilder join(String table, String condition) {
                query.append(" JOIN ")
                        .append(table)
                        .append(" ON ")
                        .append(condition);
                return this;
            }

            public SQLQueryBuilder orderBy(String... columns) {
                query.append(" ORDER BY ")
                        .append(String.join(", ", columns));
                return this;
            }

            public SQLQueryBuilder limit(int limit) {
                query.append(" LIMIT ")
                        .append(limit);
                return this;
            }

            // Finalize build

            public String build() {
                return query.toString().trim();
            }

            // Tests - Sample Usages

            public static void main(String... args) {

                String selectQuery = SQLQueryBuilder.create()
                        .select("id", "name", "email")
                        .from("users")
                        .where("age > 18")
                        .orderBy("name")
                        .limit(10)
                        .build();

                String insertQuery = SQLQueryBuilder.create()
                        .insertInto("users", "name", "email", "age")
                        .values("John Doe", "john@doe.com", 30)
                        .build();

                String updateQuery = SQLQueryBuilder.create()
                        .update("users")
                        .set("name", "Jane Doe")
                        .where("id = 1")
                        .build();

                String deleteQuery = SQLQueryBuilder.create()
                        .deleteFrom("users")
                        .where("id = 1")
                        .build();

                System.out.println("Select Query: " + selectQuery);
                System.out.println("Insert Query: " + insertQuery);
                System.out.println("Update Query: " + updateQuery);
                System.out.println("Delete Query: " + deleteQuery);

            }

        }

        /*

        Here’s a SQLQueryBuilder class using the functor pattern for building SQL queries.
        Instead of returning this within each method, each method returns a new function,
        so each step can be invoked independently and then called again as needed for flexible chaining.

        Explanation of the Functor Pattern in SQLQueryBuilder

        Each method in SQLQueryBuilder returns a Supplier<SQLQueryBuilder> rather than this.

        This allows:

        Independent Method Calls: Each part of the SQL query can be constructed by calling a method, which returns a Supplier. This function can be executed (get()) when you’re ready to proceed with building the next part.
        Separate Execution of Steps: The builder allows for each method's logic to be deferred and executed independently.

        The result is a query-building process that can be dynamically controlled, and methods can be called when needed to build SQL queries flexibly and modularly.

         */

        public class SQLBuilder1 {

            private StringBuilder query;

            // private Constructor to control the building process
            private SQLBuilder1(String initialQuery) {
                this.query = new StringBuilder(initialQuery);
            }

            // TODO: ALL SQL Query Starter methods should be static
            // * static Methods to start SQL queries
            // todo: Fix new-object instantiation in static env

            public static Supplier<SQLBuilder1> select(String... columns) {
                return () -> new SQLBuilder1("SELECT " + String.join(", ", columns));
            }

            public Supplier<SQLBuilder1> insertInto(String table, String... columns) {
                return () -> new SQLBuilder1(("INSERT INTO " + table + " (" + String.join(", ", columns) + ")"));
            }

            public Supplier<SQLBuilder1> update(String table) {
                return () -> new SQLBuilder1("UPDATE " + table + " SET");
            }

            public Supplier<SQLBuilder1> deleteFrom(String table) {
                return () -> new SQLBuilder1("DELETE FROM " + table);
            }

            // * Methods to add SQL Clauses

            public Supplier<SQLBuilder1> values(Object... values) {
                return () -> {
                    query.append(" VALUES (");
                    /*
                    values.stream().map(
                            (value, i) -> {
                                query.append("?");
                                if (i < values.length - 1)
                                    query.append(", ");
                            }
                    );
                     */
                    for (int i = 0; i < values.length; i++) {
                        query.append("?");
                        if (i < values.length - 1)
                            query.append(", ");
                    }
                    query.append(")");
                    return this;
                };
            }

            public Supplier<SQLBuilder1> set(String column, Object value) {
                return () -> {
                    if (query.toString().endsWith("SET"))
                        query.append(" ").append(column).append(" = ?");
                    else query.append(", ").append(column).append(" = ?");
                    return this;
                };
            }

            public Supplier<SQLBuilder1> where(String condition) {
                return () -> {
                    query.append(" WHERE ").append(condition);
                    return this;
                };
            }

            public Supplier<SQLBuilder1> join(String table, String condition) {
                return () -> {
                    query.append(" JOIN ").append(table).append(" ON ").append(condition);
                    return this;
                };
            }

            public Supplier<SQLBuilder1> orderBy(String... columns) {
                return () -> {
                    query.append(" ORDER BY ").append(String.join(", ", columns));
                    return this;
                };
            }

            public Supplier<SQLBuilder1> limit(int limit) {
                return () -> {
                    query.append(" LIMIT ").append(limit);
                    return this;
                };
            }

            // Finalize build

            public Supplier<String> build() {
                return () -> query.toString().trim();
            }

            // Tests - Sample Usages

            public static void main(String... args) {

                Supplier<SQLBuilder1> selectQuery =
                        SQLBuilder1.select("id", "name", "email")
                                .get().where("age > 18")
                                .get().orderBy("name")
                                .get().limit(10);

                System.out.println("Select Query: " + selectQuery.get().build().get());

                Supplier<SQLBuilder1> insertQuery =
                        SQLBuilder1.insertInto("users", "name", "email", "age")
                                .get().values("John Doe", "john@doe.com", 30);

                System.out.println("Insert Query: " + insertQuery.get().build().get());

            }

        }

        /*

        Creating a forced sequence of lambdas for a SQLQueryBuilder lets us return lambdas
        from each method that immediately direct to the next logical method.
        Here’s how we can design it so each step guides you to the next, keeping the order and readability:

        Explanation

        Inner Classes for Steps: Each part of the query process is encapsulated in an inner class like Where, Values, OrderBy, etc.
        Returning Lambdas: Each method in an inner class returns a Supplier for the next logical step. For instance, where() returns a Supplier<OrderBy>.
        Sequential Building: This approach ensures each method is called in a sequence, enforcing the intended order.

        Advantages of This Pattern

        Clear Readability: The code reads in a logical flow.
        Flexibility: This forced sequence allows certain steps to be skipped when not applicable (e.g., no WHERE in SELECT).
        Compile-Time Safety: This design helps avoid out-of-order SQL building errors at compile time.

        This design enforces an order while providing flexibility to build different types of SQL queries.

         */

        public class SQLBuilder2 {

            private final StringBuilder query;

            private SQLBuilder2(String initialQuery) {
                this.query = new StringBuilder(initialQuery);
            }

            // TODO: ALL SQL Query Starter methods should be static
            // * static Methods to start SQL queries
            // todo: Fix new-object instantiation in static env

            public static Supplier<Where> select(String... columns) {
                return () -> new SQLBuilder2(
                        "SELECT " + String.join(", ", columns)
                ).new Where();
            }

            public Supplier<Values> insertInto(String table, String... columns) {
                return () -> new SQLBuilder2(
                        "INSERT INTO "
                                + table
                                + " ("
                                + String.join(", ", columns)
                                + ")"
                ).new Values();
            }

            public Supplier<SetValues> update(String table) {
                return () -> new SQLBuilder2(
                        "UPDATE " + table + " SET"
                ).new SetValues();
            }

            public Supplier<Where> deleteFrom(String table) {
                return () -> new SQLBuilder2(
                        "DELETE FROM " + table
                ).new Where();
            }

            // Inner classes representing each step

            public class Where {
                public Supplier<OrderBy> where(String condition) {
                    query.append(" WHERE ").append(condition);
                    return OrderBy::new;
                }
            }

            public class Values {
                public Supplier<Build> values(Object... values) {
                    query.append(" VALUES (");
                    /*
                    values.stream().map(
                            (value, i) -> {
                                query.append("?");
                                if (i < values.length - 1)
                                    query.append(", ");
                            }
                    )
                     */
                    for (int i = 0; i < values.length; i++) {
                        query.append("?");
                        if (i < values.length - 1)
                            query.append(", ");
                    }
                    query.append(")");
                    return Build::new;
                }
            }

            public class SetValues {
                public Supplier<Where> set(String column, Object value) {
                    if (query.toString().endsWith("SET"))
                        query.append(" ").append(column).append(" = ?");
                    else query.append(", ").append(column).append(" = ?");
                    return Where::new;
                }
            }

            public class OrderBy {
                public Supplier<Limit> orderBy(String... columns) {
                    query.append(" ORDER BY ").append(String.join(", ", columns));
                    return Limit::new;
                }
            }

            public class Limit {
                public Supplier<Build> limit(int limit) {
                    query.append(" LIMIT ").append(limit);
                    return Build::new;
                }
            }

            // Finalize build

            public class Build {
                public String build() {
                    return query.toString().trim();
                }
            }

            // Tests - Sample Usages

            public static void main(String... args) {

                String selectQuery = SQLBuilder2.select("id", "name", "email")
                        .get().where("age > 18")
                        .get().orderBy("name")
                        .get().limit(10)
                        .get().build();

                System.out.println("Select Query: " + selectQuery);

                String insertQuery = SQLBuilder2.insertInto("users", "name", "email", "age")
                        .get().values("John Doe", "john@doe.com", 30)
                        .get().build();

                System.out.println("Insert Query: " + insertQuery);

            }

        }

        /*

        Here’s an updated SQL Query Builder class that follows the classic Builder Pattern
        by returning this after each method call, allowing you to chain methods naturally for building up SQL queries.
        In addition, this implementation demonstrates usage of Spring’s JdbcTemplate for executing CRUD operations using the built SQL string.

        Explanation of Code

        SQL Query Building: Each method in SQLQueryBuilder appends a part of the SQL query to StringBuilder and stores parameters for later binding in JdbcTemplate.
        CRUD Operations: The execute* methods (e.g., executeInsert, executeSelect) call the build() method to get the final SQL string and execute it with JdbcTemplate.
        Usage of JdbcTemplate: The jdbcTemplate is used in the UserService methods to interact with an Oracle database. Each SQL operation (SELECT, INSERT, UPDATE, DELETE) is shown with sample code.

        This setup provides a flexible SQL builder pattern combined with Spring’s JdbcTemplate, allowing you to construct and execute SQL queries efficiently.

         */

        // ! @Component
        public class SQLBuilder3 { // ! JDBC Template Example

            private final StringBuilder query = new StringBuilder();
            private final List<Object> parameters = new ArrayList<>();

            // * SQL Query Starters - select, insert-into, update, delete-from

            public SQLBuilder3 select(String... columns) {
                query.append("SELECT ").append(String.join(", ", columns)).append(" ");
                return this;
            }

            public SQLBuilder3 insertInto(String table, String... columns) {
                query.append("INSERT INTO ").append(table).append(" (").append(String.join(", ", columns)).append(") ");
                return this;
            }

            public SQLBuilder3 update(String table) {
                query.append("UPDATE ").append(table).append(" SET ");
                return this;
            }

            public SQLBuilder3 deleteFrom(String table) {
                query.append("DELETE FROM ").append(table).append(" ");
                return this;
            }

            // * SQL Query Clauses - from, where, set, values, order-by, limit, join

            public SQLBuilder3 from(String table) {
                query.append("FROM ").append(table).append(" ");
                return this;
            }

            public SQLBuilder3 where(String condition, Object... params) {
                query.append("WHERE ").append(condition).append(" ");
                // * params.stream().map(param -> parameters.add(param));
                for (Object param: params)
                    parameters.add(param);
                return this;
            }

            public SQLBuilder3 set(String column, Object value) {
                if (query.toString().endsWith(" SET "))
                    query.append(column).append(" = ?");
                else query.append(", ").append(column).append(" = ?");
                parameters.add(value);
                return this;
            }

            public SQLBuilder3 values(Object... values) {
                query.append("VALUES (");
                for (int i = 0; i < values.length; i++) {
                    query.append("?");
                    if (i < values.length - 1)
                        query.append(", ");
                }
                query.append(") ");
                for (Object value : values)
                    parameters.add(value);
                return this;
            }

            public SQLBuilder3 orderBy(String... columns) {
                query.append("ORDER BY ").append(String.join(", ", columns)).append(" ");
                return this;
            }

            public SQLBuilder3 limit(int limit) {
                query.append("LIMIT ").append(limit).append(" ");
                return this;
            }

            public SQLBuilder3 join(String joinType, String table, String onCondition) {
                query.append(joinType).append(" JOIN ").append(table).append(" ON ").append(onCondition).append(" ");
                return this;
            }

            // Finalize build

            public String build() {
                return query.toString().trim();
            }

            // /*

            // JDBC Template Example Usages

            public int executeInsert(JdbcTemplate jdbcTemplate) {
                return jdbcTemplate.update(build(), parameters.toArray());
            }

            public int executeUpdate(JdbcTemplate jdbcTemplate) {
                return jdbcTemplate.udpate(build(), parameters.toArray());
            }

            public List<?> executeSelect(JdbcTemplate jdbcTemplate, Class<?> elementType) {
                return jdbcTemplate.queryForList(build(), elementType, parameters.toArray());
            }

            public int executeDelete(JdbcTemplate jdbcTemplate) {
                return jdbcTemplate.update(build(), parameters.toArray());
            }

            // Tests - Sample Usages

            public static void main(String... args) {

                // * instantiated by @Annotated Dependency Injection - @Autowired
                JdbcTemplate jdbc = new JdbcTemplate();

                System.out.println("Insert: " + executeInsert(jdbc));
                System.out.println("Update: " + executeUpdate(jdbc));
                System.out.println("Select: " + executeSelect(jdbc), new Class<SomeClass>());
                System.out.println("Delete: " + executeDelete(jdbc));

            }

            // */

        }

        /*

        Usage Example with JdbcTemplate

        In your Spring application, you would use this SQLQueryBuilder class along
        with JdbcTemplate to execute queries.
        Below are examples of using the builder to create and execute SQL queries.

         */

        // ! @Service
        public class JDBCTemplate_Usage {

            // * @Autowired
            private JdbcTemplate jdbcTemplate;

            // * @Autowired
            private SQLBuilder3 sql;

            public List<?> getUsers() {
                return sql.select("id", "name", "email")
                        .from("users")
                        .where("age > ?", 18)
                        .orderBy("name")
                        .limit(10)
                        .executeSelect(jdbcTemplate, Sample.class);
            }

            public int addUser(String name, String email, int age) {
                return sql.insertInto("users", "name", "email", "age")
                        .values(name, email, age)
                        .executeInsert(jdbcTemplate);
            }

            public int updateUserEmail(int userId, String email) {
                return sql.update("users")
                        .set("email", email)
                        .where("id = ?", userId)
                        .executeUpdate(jdbcTemplate);
            }

            public int deleteUser(int userId) {
                return sql.deleteFrom("users")
                        .where("id = ?", userId)
                        .executeDelete(jdbcTemplate);
            }

        }
        

        public static void main(String[] args) {
            System.out.println(String.join(", ", args));
        }


    }
}
