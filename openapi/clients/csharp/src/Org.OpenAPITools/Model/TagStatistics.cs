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
    /// TagStatistics
    /// </summary>
    [DataContract]
    public partial class TagStatistics :  IEquatable<TagStatistics>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="TagStatistics" /> class.
        /// </summary>
        /// <param name="name">name of the tag.</param>
        /// <param name="triggers">array of trigger IDs that have this tag.</param>
        /// <param name="subscriptions">subscriptions for this tag.</param>
        public TagStatistics(string name = default(string), List<string> triggers = default(List<string>), List<Subscription> subscriptions = default(List<Subscription>))
        {
            this.Name = name;
            this.Triggers = triggers;
            this.Subscriptions = subscriptions;
        }
        
        /// <summary>
        /// name of the tag
        /// </summary>
        /// <value>name of the tag</value>
        [DataMember(Name="name", EmitDefaultValue=false)]
        public string Name { get; set; }

        /// <summary>
        /// array of trigger IDs that have this tag
        /// </summary>
        /// <value>array of trigger IDs that have this tag</value>
        [DataMember(Name="triggers", EmitDefaultValue=false)]
        public List<string> Triggers { get; set; }

        /// <summary>
        /// subscriptions for this tag
        /// </summary>
        /// <value>subscriptions for this tag</value>
        [DataMember(Name="subscriptions", EmitDefaultValue=false)]
        public List<Subscription> Subscriptions { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class TagStatistics {\n");
            sb.Append("  Name: ").Append(Name).Append("\n");
            sb.Append("  Triggers: ").Append(Triggers).Append("\n");
            sb.Append("  Subscriptions: ").Append(Subscriptions).Append("\n");
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
            return this.Equals(input as TagStatistics);
        }

        /// <summary>
        /// Returns true if TagStatistics instances are equal
        /// </summary>
        /// <param name="input">Instance of TagStatistics to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(TagStatistics input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Name == input.Name ||
                    (this.Name != null &&
                    this.Name.Equals(input.Name))
                ) && 
                (
                    this.Triggers == input.Triggers ||
                    this.Triggers != null &&
                    input.Triggers != null &&
                    this.Triggers.SequenceEqual(input.Triggers)
                ) && 
                (
                    this.Subscriptions == input.Subscriptions ||
                    this.Subscriptions != null &&
                    input.Subscriptions != null &&
                    this.Subscriptions.SequenceEqual(input.Subscriptions)
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
                if (this.Name != null)
                    hashCode = hashCode * 59 + this.Name.GetHashCode();
                if (this.Triggers != null)
                    hashCode = hashCode * 59 + this.Triggers.GetHashCode();
                if (this.Subscriptions != null)
                    hashCode = hashCode * 59 + this.Subscriptions.GetHashCode();
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
