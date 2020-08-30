/*
 * Moira Alert
 *
 * This is an API description for [Moira Alert project](https://moira.readthedocs.io/en/latest/overview.html). Please check <https://github.com/moira-alert/>
 *
 * API version: 2.5.1.48
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package openapi
// SubscriptionPlotting struct for SubscriptionPlotting
type SubscriptionPlotting struct {
	Enabled bool `json:"enabled,omitempty"`
	// Theme of the chart. Should be either 'light' or 'dark'
	Theme string `json:"theme,omitempty"`
}
