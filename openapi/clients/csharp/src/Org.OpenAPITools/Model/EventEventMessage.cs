/* 
 * Moira Alert
 *
 * This is an API description for [Moira Alert project](https://moira.readthedocs.io/en/latest/overview.html). Please check <https://github.com/moira-alert/>
 *
 * The version of the OpenAPI document: 2.5.1.48
 * 
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */

using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using OpenAPIDateConverter = Org.OpenAPITools.Client.OpenAPIDateConverter;

namespace Org.OpenAPITools.Model
{
    /// <summary>
    /// EventEventMessage
    /// </summary>
    [DataContract]
    public partial class EventEventMessage :  IEquatable<EventEventMessage>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="EventEventMessage" /> class.
        /// </summary>
        /// <param name="maintenance">maintenance.</param>
        /// <param name="interval">interval.</param>
        public EventEventMessage(EventEventMessageMaintenance maintenance = default(EventEventMessageMaintenance), int interval = default(int))
        {
            this.Maintenance = maintenance;
            this.Interval = interval;
        }
        
        /// <summary>
        /// Gets or Sets Maintenance
        /// </summary>
        [DataMember(Name="maintenance", EmitDefaultValue=false)]
        public EventEventMessageMaintenance Maintenance { get; set; }

        /// <summary>
        /// Gets or Sets Interval
        /// </summary>
        [DataMember(Name="interval", EmitDefaultValue=false)]
        public int Interval { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class EventEventMessage {\n");
            sb.Append("  Maintenance: ").Append(Maintenance).Append("\n");
            sb.Append("  Interval: ").Append(Interval).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as EventEventMessage);
        }

        /// <summary>
        /// Returns true if EventEventMessage instances are equal
        /// </summary>
        /// <param name="input">Instance of EventEventMessage to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(EventEventMessage input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Maintenance == input.Maintenance ||
                    (this.Maintenance != null &&
                    this.Maintenance.Equals(input.Maintenance))
                ) && 
                (
                    this.Interval == input.Interval ||
                    (this.Interval != null &&
                    this.Interval.Equals(input.Interval))
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.Maintenance != null)
                    hashCode = hashCode * 59 + this.Maintenance.GetHashCode();
                if (this.Interval != null)
                    hashCode = hashCode * 59 + this.Interval.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

}
