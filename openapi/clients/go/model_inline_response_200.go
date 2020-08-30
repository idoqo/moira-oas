/*
 * Moira Alert
 *
 * This is an API description for [Moira Alert project](https://moira.readthedocs.io/en/latest/overview.html). Please check <https://github.com/moira-alert/>
 *
 * API version: 2.5.1.48
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package openapi
// InlineResponse200 struct for InlineResponse200
type InlineResponse200 struct {
	// Flag for determining if Moira is accessible remotely.
	RemoteAllowed bool `json:"remoteAllowed,omitempty"`
	// List of enabled contact types
	Contacts []InlineResponse200Contacts `json:"contacts,omitempty"`
}