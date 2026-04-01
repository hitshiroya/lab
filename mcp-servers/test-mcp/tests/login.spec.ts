import { test, expect } from "@playwright/test";

// ─── Selectors ────────────────────────────────────────────────────────────────
const USERNAME_INPUT = "#username"
const PASSWORD_INPUT = "#password";
const LOGIN_BUTTON = "#login-button";
const ERROR_MESSAGE = '[data-test="error"]';
const ERROR_CLOSE_BUTTON = ".error-button";

// ─── Credentials ──────────────────────────────────────────────────────────────
const VALID_PASSWORD = "secret_sauce";

const USERS = {
  standard: "standard_user",
  lockedOut: "locked_out_user",
  problem: "problem_user",
  performanceGlitch: "performance_glitch_user",
  error: "error_user",
  visual: "visual_user",
} as const;

// ─── Helpers ──────────────────────────────────────────────────────────────────
async function login(
  page: Parameters<Parameters<typeof test>[1]>[0]["page"],
  username: string,
  password: string
) {
  await page.fill(USERNAME_INPUT, username);
  await page.fill(PASSWORD_INPUT, password);
  await page.click(LOGIN_BUTTON);
}

// ─── Test Suite ───────────────────────────────────────────────────────────────

test.describe("Swag Labs – Login Page", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/");
  });

  // ── UI & Layout ─────────────────────────────────────────────────────────────

  test.describe("UI & Layout", () => {
    test("page has correct title", async ({ page }) => {
      await expect(page).toHaveTitle("Swag Labs");
    });

    test("login form elements are visible", async ({ page }) => {
      await expect(page.locator(USERNAME_INPUT)).toBeVisible();
      await expect(page.locator(PASSWORD_INPUT)).toBeVisible();
      await expect(page.locator(LOGIN_BUTTON)).toBeVisible();
    });

    test("username input has correct placeholder", async ({ page }) => {
      await expect(page.locator(USERNAME_INPUT)).toHaveAttribute(
        "placeholder",
        "Username"
      );
    });

    test("password input has correct placeholder", async ({ page }) => {
      await expect(page.locator(PASSWORD_INPUT)).toHaveAttribute(
        "placeholder",
        "Password"
      );
    });

    test("password field masks input", async ({ page }) => {
      await expect(page.locator(PASSWORD_INPUT)).toHaveAttribute(
        "type",
        "password"
      );
    });

    test("login button has correct label", async ({ page }) => {
      await expect(page.locator(LOGIN_BUTTON)).toHaveValue("Login");
    });

    test("page displays the Swag Labs logo", async ({ page }) => {
      const logo = page.locator(".login_logo");
      await expect(logo).toBeVisible();
      await expect(logo).toContainText("Swag Labs");
    });

    test("accepted usernames list is visible", async ({ page }) => {
      const usernameList = page.locator("#login_credentials");
      await expect(usernameList).toBeVisible();
    });

    test("accepted passwords list is visible", async ({ page }) => {
      const passwordList = page.locator(".login_password");
      await expect(passwordList).toBeVisible();
    });
  });

  // ── Successful Login ─────────────────────────────────────────────────────────

  test.describe("Successful Login", () => {
    test("standard_user can log in and reaches inventory page", async ({
      page,
    }) => {
      await login(page, USERS.standard, VALID_PASSWORD);
      await expect(page).toHaveURL(/.*inventory/);
    });

    test("problem_user can log in and reaches inventory page", async ({
      page,
    }) => {
      await login(page, USERS.problem, VALID_PASSWORD);
      await expect(page).toHaveURL(/.*inventory/);
    });

    test("performance_glitch_user can log in (with extended timeout)", async ({
      page,
    }) => {
      await login(page, USERS.performanceGlitch, VALID_PASSWORD);
      await expect(page).toHaveURL(/.*inventory/, { timeout: 15000 });
    });

    test("error_user can log in and reaches inventory page", async ({
      page,
    }) => {
      await login(page, USERS.error, VALID_PASSWORD);
      await expect(page).toHaveURL(/.*inventory/);
    });

    test("visual_user can log in and reaches inventory page", async ({
      page,
    }) => {
      await login(page, USERS.visual, VALID_PASSWORD);
      await expect(page).toHaveURL(/.*inventory/);
    });

    test("inventory page title is visible after login", async ({ page }) => {
      await login(page, USERS.standard, VALID_PASSWORD);
      await expect(page.locator(".title")).toContainText("Products");
    });
  });

  // ── Failed Login ─────────────────────────────────────────────────────────────

  test.describe("Failed Login", () => {
    test("shows error for empty username and password", async ({ page }) => {
      await page.click(LOGIN_BUTTON);
      await expect(page.locator(ERROR_MESSAGE)).toBeVisible();
      await expect(page.locator(ERROR_MESSAGE)).toContainText(
        "Username is required"
      );
    });

    test("shows error for missing password", async ({ page }) => {
      await page.fill(USERNAME_INPUT, USERS.standard);
      await page.click(LOGIN_BUTTON);
      await expect(page.locator(ERROR_MESSAGE)).toBeVisible();
      await expect(page.locator(ERROR_MESSAGE)).toContainText(
        "Password is required"
      );
    });

    test("shows error for missing username", async ({ page }) => {
      await page.fill(PASSWORD_INPUT, VALID_PASSWORD);
      await page.click(LOGIN_BUTTON);
      await expect(page.locator(ERROR_MESSAGE)).toBeVisible();
      await expect(page.locator(ERROR_MESSAGE)).toContainText(
        "Username is required"
      );
    });

    test("shows error for wrong password", async ({ page }) => {
      await login(page, USERS.standard, "wrong_password");
      await expect(page.locator(ERROR_MESSAGE)).toBeVisible();
      await expect(page.locator(ERROR_MESSAGE)).toContainText(
        "Username and password do not match"
      );
    });

    test("shows error for wrong username", async ({ page }) => {
      await login(page, "invalid_user", VALID_PASSWORD);
      await expect(page.locator(ERROR_MESSAGE)).toBeVisible();
      await expect(page.locator(ERROR_MESSAGE)).toContainText(
        "Username and password do not match"
      );
    });

    test("shows error for completely wrong credentials", async ({ page }) => {
      await login(page, "bad_user", "bad_password");
      await expect(page.locator(ERROR_MESSAGE)).toBeVisible();
    });

    test("does not navigate away from login page on failed login", async ({
      page,
    }) => {
      await login(page, "bad_user", "bad_password");
      await expect(page).toHaveURL("https://www.saucedemo.com/");
    });

    test("locked_out_user sees account locked error", async ({ page }) => {
      await login(page, USERS.lockedOut, VALID_PASSWORD);
      await expect(page.locator(ERROR_MESSAGE)).toBeVisible();
      await expect(page.locator(ERROR_MESSAGE)).toContainText(
        "Sorry, this user has been locked out"
      );
    });

    test("locked_out_user is not redirected to inventory", async ({ page }) => {
      await login(page, USERS.lockedOut, VALID_PASSWORD);
      await expect(page).not.toHaveURL(/.*inventory/);
    });
  });

  // ── Error Message Behaviour ───────────────────────────────────────────────────

  test.describe("Error Message Behaviour", () => {
    test("error message can be dismissed with the close button", async ({
      page,
    }) => {
      await page.click(LOGIN_BUTTON);
      await expect(page.locator(ERROR_MESSAGE)).toBeVisible();
      await page.click(ERROR_CLOSE_BUTTON);
      await expect(page.locator(ERROR_MESSAGE)).not.toBeVisible();
    });

    test("input fields get error styling on failed login", async ({ page }) => {
      await page.click(LOGIN_BUTTON);
      await expect(page.locator(USERNAME_INPUT)).toHaveClass(/error/);
      await expect(page.locator(PASSWORD_INPUT)).toHaveClass(/error/);
    });

    test("error styling is removed after dismissing the error", async ({
      page,
    }) => {
      await page.click(LOGIN_BUTTON);
      await page.click(ERROR_CLOSE_BUTTON);
      await expect(page.locator(USERNAME_INPUT)).not.toHaveClass(/error/);
      await expect(page.locator(PASSWORD_INPUT)).not.toHaveClass(/error/);
    });
  });

  // ── Input Behaviour ───────────────────────────────────────────────────────────

  test.describe("Input Behaviour", () => {
    test("username field accepts typed text", async ({ page }) => {
      await page.fill(USERNAME_INPUT, USERS.standard);
      await expect(page.locator(USERNAME_INPUT)).toHaveValue(USERS.standard);
    });

    test("username field can be cleared", async ({ page }) => {
      await page.fill(USERNAME_INPUT, USERS.standard);
      await page.fill(USERNAME_INPUT, "");
      await expect(page.locator(USERNAME_INPUT)).toHaveValue("");
    });

    test("login can be triggered by pressing Enter in the password field", async ({
      page,
    }) => {
      await page.fill(USERNAME_INPUT, USERS.standard);
      await page.fill(PASSWORD_INPUT, VALID_PASSWORD);
      await page.press(PASSWORD_INPUT, "Enter");
      await expect(page).toHaveURL(/.*inventory/);
    });

    test("credentials are case-sensitive (wrong case fails)", async ({
      page,
    }) => {
      await login(page, "Standard_User", VALID_PASSWORD);
      await expect(page.locator(ERROR_MESSAGE)).toBeVisible();
    });

    test("whitespace-only username shows an error", async ({ page }) => {
      await page.fill(USERNAME_INPUT, "   ");
      await page.fill(PASSWORD_INPUT, VALID_PASSWORD);
      await page.click(LOGIN_BUTTON);
      await expect(page.locator(ERROR_MESSAGE)).toBeVisible();
    });
  });

  // ── Accessibility ─────────────────────────────────────────────────────────────

  test.describe("Accessibility", () => {
    test("username input is focusable via keyboard Tab", async ({ page }) => {
      await page.keyboard.press("Tab");
      await expect(page.locator(USERNAME_INPUT)).toBeFocused();
    });

    test("focus moves from username to password with Tab", async ({ page }) => {
      await page.focus(USERNAME_INPUT);
      await page.keyboard.press("Tab");
      await expect(page.locator(PASSWORD_INPUT)).toBeFocused();
    });

    test("login button is reachable via keyboard", async ({ page }) => {
      await page.focus(USERNAME_INPUT);
      await page.keyboard.press("Tab");
      await page.keyboard.press("Tab");
      await expect(page.locator(LOGIN_BUTTON)).toBeFocused();
    });
  });
});
